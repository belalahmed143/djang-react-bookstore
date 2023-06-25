import React, { useEffect, useState } from 'react'
import axios from "axios";
import { addToCartURL, bookDetailURL } from "../endpoint";
import { useParams } from 'react-router-dom'

const BookDetail = () => {
    const {id} = useParams()

    const [book, setBook] = useState([])

    useEffect(()=>{
      async function getBook(){
        try {
          const book = await axios.get(bookDetailURL+`${id}/`)
          setBook(book.data)
        } catch (error) {
        //   console.log(error)
        }
      }getBook()
    },[id])

    const username = "admin";
    const password = "admin";
    const url = addToCartURL;
  
    const headers = {"Content-Type": "application/json"};

  
    function handleClick() {
      axios.post(url, {id}, {headers: headers, auth: {username: username, password: password}})
        .then(response => {
          console.log(response.data);
          console.log(response.status);
        })
        .catch(error => {
          console.error(error);
        });
    }

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-5">
                    <img src={book.image} alt="" style={{width:'100%'}} />
                </div>
                <div className="col-md-7">             
                    <div className="card-body">
                        <h5>{book.name}</h5>
                        <p>
                            {book.discount_price?
                                <>
                                Price:{book.discount_price}
                                <br /><del>{book.price}</del>
                                </>
                            : <>Price {book.price}</>
                            }
                            </p>
                        <p dangerouslySetInnerHTML={{__html: book.discription}} />
                        <button onClick={handleClick}>Add to cart</button>
                    </div>
                </div>
            </div>
            
        </div>
      
    );
}

export default BookDetail
