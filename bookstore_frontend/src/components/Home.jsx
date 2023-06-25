import React, { useEffect, useState } from 'react'
import { bookListURL } from '../endpoint'
import axios from 'axios'
import { Link } from 'react-router-dom';


const Home = () => {
    const [books, setBooks] = useState([])

    useEffect(()=>{
    async function getBooks(){
        try {
        const books = await axios.get(bookListURL)
        setBooks(books.data)
        console.log(books.data)
        } catch (error) {
        // console.log(error)
        }
    }getBooks()
    },[])

  return (
    <div>
        <div className='container'>
            <h3>Best For You</h3>
            <div className='row'>
                {
                    books.map((book,i) =>{
                        return(
                            <div className="col-md-4 d-flex align-items-stretch" key={i}>
                                <div className="card shadow-lg">
                                    <img src={book.image} alt="" />
                                    <div className="card-body">
                                        <h5>{book.name}</h5>
                                        <p>
                                            {book.discount_price?
                                                <>
                                                Price: {book.discount_price}
                                                <br /><del>{book.price}</del>
                                                </>
                                            : <p>Price {book.price}</p>
                                            }
                                            </p>
                                        <Link className='btn btn-sm btn-info' to={`/book-detail/${book.id}`}>View</Link>
                                    </div>
                                </div>
                            </div>
                        )
                    })
                }
            </div>
        </div>
    </div>
  )
}

export default Home