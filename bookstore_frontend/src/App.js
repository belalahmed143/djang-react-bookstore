import {BrowserRouter, Route, Switch} from "react-router-dom"
import Navbar from './components/Navbar'
import Home from "./components/Home";
import BookDetail from "./components/BookDetail";
import CartSummary from "./components/CartSummary";
function App() {
  return (
    <div>
      <BrowserRouter>
        <Navbar />
          <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/book-detail/:id" component={BookDetail} />
          <Route exact path="/cart-summary" component={CartSummary} />
          </Switch>
          
      </BrowserRouter>
    </div>
  );
}

export default App;
