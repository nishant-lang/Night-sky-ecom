


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



document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.form-btn');

    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();  // Stop normal form submission

            const url = form.action;  // Get the form action URL
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({}),  // No data needed if backend just needs product_id from URL
            })
            .then(response => response.json().then(data => ({status: response.status, body: data})))
            .then(({status, body}) => {
                if (status === 200) {
                    showToast(body.message, 'success');
                } else {
                    showToast(body.message || 'Failed to add to cart.', 'error');
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);
                showToast('Something went wrong. Try again!', 'error');
            });
        });
    }

    function showToast(message, type) {
        const toast = document.createElement('div');
        toast.textContent = message;
        toast.style.position = 'fixed';
        toast.style.bottom = '20px';
        toast.style.right = '20px';
        toast.style.backgroundColor = type === 'success' ? '#4CAF50' : '#f44336';
        toast.style.color = '#fff';
        toast.style.padding = '12px 20px';
        toast.style.borderRadius = '8px';
        toast.style.boxShadow = '0px 0px 10px rgba(0,0,0,0.3)';
        toast.style.zIndex = '1000';
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }
});