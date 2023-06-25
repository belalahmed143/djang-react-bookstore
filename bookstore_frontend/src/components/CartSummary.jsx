import React, { useEffect, useState } from 'react'
import { CartSummaryURL } from '../endpoint';
import axios from 'axios'

const CartSummary = () => {

    const username = "admin";
    const password = "admin";
    const url = CartSummaryURL;
    const headers = {"Content-Type": "application/json"};

    const [cartitem, setCartSummary] = useState([])

    useEffect(()=>{
    async function getCartSummary(){
        try {
        const cartitem = await axios.get(url, {headers: headers, auth: {username: username, password: password}})
        setCartSummary(cartitem.data)
        console.log(cartitem.data)
        } catch (error) {
        console.log(error)
        }
    }getCartSummary()
    },[])


  return (
    <div>
            {cartitem?   
            <div>
                {cartitem && (
                  
                  <div className=''>
                    {cartitem.total >0?
                    <div className='card p-2'>
                     <div className='row'>
                     <h5 className='mt-3'>Cart Summary</h5> 
                     <div className='col-md-7 order-2 order-md-1'>
                          {cartitem.books.map((b, i) => {
                            return (                             
                              <div className='card order-summary-card shadow p-1' key={i}>
                              <div className='row'>
                                  <div className='col-4 my-auto'>
                                    <img src={`http://127.0.0.1:8000${b.book.image}`} alt="" style={{width:'100px'}} />
                                  </div>
                                  <div className='col-8 text-center my-auto'>
                                    <p className='fw-bold fs-6'>{b.book.name}</p>
                                    <p>
                                        {b.book.discount_price?
                                            <>
                                            Price:{b.book.discount_price}
                                            <br /><del>{b.book.price}</del>
                                            </>
                                        : <>Price {b.book.price}</>
                                        }
                                        </p>
                                        <p>Quantity : {b.quantity}</p>
                                  </div>
                                </div>
                              
                              </div>                      
                            );
                          })}
                      </div>

                      <div className='col-md-5 order-1 order-md-2'>
                          <div className='card p-2'>
                            <h6>Cart Total</h6><hr />
                          <table className="table table-dark">
                            <tfoot>
                            <tr>
                            <td>Total</td>
                            <td className='text-end'>{cartitem.total} BDT</td>
                            </tr>
                            </tfoot>  
                          </table>
                          </div>
                      </div>

                    </div>
                    </div>
                    :<h3 className='text-center'>Your cart is empty</h3>
                    }
                  </div>
                )}
            </div>
            :<h3 className='text-center'>Your cart is empty</h3>
          }
    </div>
  )
}

export default CartSummary