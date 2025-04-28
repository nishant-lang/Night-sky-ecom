

// document.addEventListener("DOMContentLoaded", function() {
  
//   const productPic = document.querySelector(".product-pic");
//   const prevBtn = document.querySelector(".prev-btn");
//   const nextBtn = document.querySelector(".next-btn");

//   console.log(productPic)
//   console.log(prevBtn)
//   console.log(nextBtn)

//   const scrollAmount = 550 // Adjust based on image width

//   nextBtn.addEventListener("click", function() {
//       productPic.scrollBy({ left: scrollAmount, behavior: "smooth" });
//       console.log('next btn clicked')
//   });

//   prevBtn.addEventListener("click", function() {
//       productPic.scrollBy({ left: -scrollAmount, behavior: "smooth" });
//       console.log('prev btn clicked')
//   });
// });


// document.addEventListener("DOMContentLoaded", function() {
//   const productPic = document.querySelector(".product-pic");
//   const prevBtn = document.querySelector(".prev-btn");
//   const nextBtn = document.querySelector(".next-btn");

//   function getImageWidth() {
//       return productPic.querySelector("img").clientWidth; // Get exact image width
//   }

//   nextBtn.addEventListener("click", function() {
//       productPic.scrollBy({ left: getImageWidth(), behavior: "smooth" });
//   });

//   prevBtn.addEventListener("click", function() {
//       productPic.scrollBy({ left: -getImageWidth(), behavior: "smooth" });
//   });
// });




document.addEventListener("DOMContentLoaded", function() {

  const productPic = document.querySelector(".product-pic");
  const prevBtn = document.querySelector(".prev-btn");
  const nextBtn = document.querySelector(".next-btn");
  const dotsContainer = document.querySelector(".dots-container");

  const images = productPic.querySelectorAll("img");

  let index = 0; // Track current image index

  // Create dots dynamically
  images.forEach((_, i) => {
      const dot = document.createElement("div");
      dot.classList.add("dot");
      if (i === 0) dot.classList.add("active");
      dot.dataset.index = i;
      dotsContainer.appendChild(dot);
  });

  const dots = document.querySelectorAll(".dot");

  function scrollToImage() {
    
      const imgWidth = images[0].clientWidth;
      productPic.scrollTo({ left: index * imgWidth, behavior: "smooth" });

      // Update active dot
      dots.forEach(dot => dot.classList.remove("active"));
      dots[index].classList.add("active");
  }

  nextBtn.addEventListener("click", function() {
      if (index < images.length - 1) {
          index++;
          scrollToImage();
      }
  });

  prevBtn.addEventListener("click", function() {
      if (index > 0) {
          index--;
          scrollToImage();
      }
  });

  // Click on dots to navigate images
  dots.forEach(dot => {
      dot.addEventListener("click", function() {
          index = parseInt(this.dataset.index);
          scrollToImage();
      });
  });
});



// document.addEventListener("DOMContentLoaded", function () {
//     const paymentRadios = document.querySelectorAll("input[name='payment-method']");
//     const paymentSections = {
//         upi: document.querySelector(".upi-payment"),
//         card: document.querySelector(".card-payment")
//     };

//     function updatePaymentView() {
//         Object.values(paymentSections).forEach(section => section.style.display = "none");
//         const selectedPayment = document.querySelector("input[name='payment-method']:checked").value;
//         paymentSections[selectedPayment].style.display = "block";
//     }

//     paymentRadios.forEach(radio => radio.addEventListener("change", updatePaymentView));
// });



document.addEventListener("DOMContentLoaded", function () {
    const paymentRadios = document.querySelectorAll("input[name='payment-method']");
    const paymentSections = {
        upi: document.querySelector(".upi-payment"),
        card: document.querySelector(".card-payment")
    };

    function updatePaymentView() {
        Object.values(paymentSections).forEach(section => section.style.display = "none");
        const selectedPayment = document.querySelector("input[name='payment-method']:checked").value;
        paymentSections[selectedPayment].style.display = "block";

        // Redirect to checkout page if card is selected
        if (selectedPayment === "card") {
            window.location.href = "/payment/checkout/";  // Change URL if needed
        }
    }
    paymentRadios.forEach(radio => radio.addEventListener("change", updatePaymentView));
});


// document.addEventListener("DOMContentLoaded", function () {
//     const buyButton = document.getElementById("bye");
//     console.log('buybtn clicked....')
//     buyButton.addEventListener('click', function () {
//         const productId = buyButton.getAttribute("data-product-id");
        
//         if (productId) {
//             window.location.href = `/payment/create-checkout-session/${productId}`;
//         } else {
//             console.error("Product ID not found!");
//         }
//     });
// });








// document.addEventListener("DOMContentLoaded", function() {
//     // Get references to the previous and next buttons
//     var prevButton = document.querySelector('.carousel-control-prev');
//     var nextButton = document.querySelector('.carousel-control-next');
    
//     // Get a reference to the carousel element
//     var carousel = document.getElementById('productCarousel');

//     // Add click event listener for the "Previous" button
//     prevButton.addEventListener('click', function() {
//         var carouselInstance = new bootstrap.Carousel(carousel);
//         carouselInstance.prev();
//     });

//     // Add click event listener for the "Next" button
//     nextButton.addEventListener('click', function() {
//         var carouselInstance = new bootstrap.Carousel(carousel);
//         carouselInstance.next();
//     });
// });



// // Get a reference to the "Add to Cart" button

// const addToCartButton = document.querySelector('.addToCartBtn');

// // Add a click event listener to the button
// addToCartButton.addEventListener('click', function() {
// // Get the product ID from the data attribute
// const productId = this.getAttribute('data-product-id');
// const csrftoken='{{csrftoken}}'
// console.log('Product ID:', productId);

// fetch(`http://127.0.0.1:8000/bayer/add-to-cart/${productId}/`,{

//   method:"POST",
//   headers:{'X-CSRFToken':csrftoken,},
//   //body:formData,
//   credential:'same-origin',
 
// }).then(response => {
//   console.log(response.status)
//   return response.json()
  
  
//   //return get_blog_post()
// }).then((data)=>{
//   console.log(data)
//   if (data.hasOwnProperty('message')){

//   }
// })

// });

