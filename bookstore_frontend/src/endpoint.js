const localhost = "http://127.0.0.1:8000"
const apiURL = '/api'

export const endpoint = `${localhost}${apiURL}`;

export const bookListURL = `${endpoint}/book-store/`;
export const bookDetailURL = `${endpoint}/book-detail/`;
export const addToCartURL = `${endpoint}/add-to-cart/`;
export const CartSummaryURL = `${endpoint}/cart-summary/`;