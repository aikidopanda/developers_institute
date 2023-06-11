import React, { Component } from 'react';
import { Carousel } from 'react-responsive-carousel'
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import "react-responsive-carousel/lib/styles/carousel.min.css";

class SampleCarousel extends Component {
  render() {
      return (
          <Carousel width="40%">
              <div>
                  <img src="Hongkong.jpg" alt="Hongkong" />
                  <p className="legend">Hongkong</p>
              </div>
              <div>
                  <img src="Macao.webp" alt="Macao" />
                  <p className="legend">Macao</p>
              </div>
              <div>
                  <img src="Japan.webp" alt="Japan"/>
                  <p className="legend">Japan</p>
              </div>
              <div>
                  <img src="Las-Vegas.webp" alt="Las-Vegas"/>
                  <p className="legend">Las-Vegas</p>
              </div>
          </Carousel>
      );
  }
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <SampleCarousel />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
