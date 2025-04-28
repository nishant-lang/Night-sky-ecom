
window.onload = function() {
   
    // This code will execute when the page is fully loaded.
   
    const csrftoken='{{csrftoken}}'
    const cart_body=document.getElementById('cart-body')

    console.log('csrfttoken:', csrftoken);

    fetch(`http://127.0.0.1:8000/bayer/user-cart/`,{

      method:"GET",
      headers:{"Content-Type":"application/json"},
      credential:'same-origin',
     
    }).then(response => {
      console.log(response.status)
      return response.json()
       
      //return get_blog_post()
    }).then((data)=>{
      //console.log(typeof(data))
    const renderHtml = function (item){
      console.log(item)

    const html=

          `<div class="card-body  border-bottom"  >      
          <blockquote class="blockquote mb-0">
            <div class="d-flex"> 
              <img style="height: 150px; width:120px" src="${item.product_pic}" alt="....">
              <div class="ml-4" style="height: 150px;">
                <p style="font-family: 'Times New Roman', Times, serif; color: rgb(70, 61, 61);">${item.name}</p>
                <div style="font-family: 'Times New Roman', Times, serif; color: rgb(182, 193, 193); font-size: 18px;">
                <p>Size : L <br>Seller : Emart Retail <br>Price : ₹ ${item.price}</p>
                </div> 
            </div>
            
            </blockquote>
            <div class="d-flex">
            <div  style="margin-left: 142px;">
              <a href="" style="color: rgb(32, 31, 31);text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='blue'" onmouseout="this.style.color='rgb(32, 31, 31)'">SAVE FOR LATER</a>
            </div>
          
            <div style="margin-left: 30px;">
              <a href="javascript:RemoveFunction(${item.id});" style="color: rgb(32, 31, 31); text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='blue'" onmouseout="this.style.color='rgb(32, 31, 31)'">REMOVE</a>
            </div>
          </div>
           
        </div>
      </div>`

      ;
      cart_body.insertAdjacentHTML("beforeend", html);
    }
    
    for (let i = 0; i < data.length; i++) {
      console.log(data[i])
      renderHtml(data[i]); 
    }

    })
  };



  function RemoveFunction(id){
    
    const csrftoken='{{csrftoken}}'
    const cart_body=document.getElementById('cart-body')

    console.log('csrfttoken:', csrftoken);

    fetch(`http://127.0.0.1:8000/bayer/remove-cart-product/${id}`,{

      method:"GET",
      headers:{"Content-Type":"application/json"},
      credential:'same-origin',
     
    }).then(response => {
      console.log(response.status)
      return response.json()
       
      //return get_blog_post()
    }).then((data)=>{
      console.log(data)
    const renderHtml = function (item){
      console.log(item)
    }
  })

   // console.log(id)
   // console.log('Hello This is the remove function...clicked')
  }