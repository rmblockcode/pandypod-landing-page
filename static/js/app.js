window.addEventListener('load', function() {
    new Glider(document.querySelector('.carousel__list'), {
        slidesToShow: 1,
        slidesToScroll: 1,
        draggable: true,
        duration: 1.5,
        dots: '.carousel__indicators',
        arrows: {
            prev: '.carousel__previous',
            next: '.carousel__next'
        },
        responsive: [
            {
              // screens greater than >= 775px
              breakpoint: 450,
              settings: {
                // Set to `auto` and provide item width to adjust to viewport
                slidesToShow: 2,
                slidesToScroll: 2
            }
            },{
              // screens greater than >= 1024px
              breakpoint: 800,
              settings: {
                slidesToShow: 4,
                slidesToScroll: 4
              }
            }
        ]
    });
    
});

const formResponse = document.querySelector('.footer__form--response');
const subscriptionForm = document.querySelector('#footer__subscription-form');

subscriptionForm.addEventListener('submit', function(e){
  e.preventDefault();

  first_name = document.querySelector('#id_first_name').value;
  last_name = document.querySelector('#id_last_name').value;
  email = document.querySelector('#id_email').value;

  const formData = new FormData(subscriptionForm);

  fetch("/subscription", {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    // Show response
    if (!data.hasOwnProperty('error')){
      // Clear the form
      subscriptionForm.reset();

      const isFormError = formResponse.classList.contains('footer__form--error');

      if (isFormError) formResponse.classList.remove('footer__form--error');

      formResponse.innerHTML = data.message;
      formResponse.classList.add('footer__form--success');
    }else{
      const isFormSuccess = formResponse.classList.contains('footer__form--success');

      if (isFormSuccess) formResponse.classList.remove('footer__form--success');

      formResponse.innerHTML = data.error;
      formResponse.classList.add('footer__form--error');
    }

  })
  .catch((error) => {
    // TODO: make helper function for repeated code
    const isFormSuccess = formResponse.classList.contains('footer__form--success');

    if (isFormSuccess) formResponse.classList.remove('footer__form--success');

    formResponse.innerHTML = error;
    formResponse.classList.add('footer__form--error');
  });
});

function reveal() {
  var reveals = document.querySelectorAll(".reveal");

  reveals.forEach((reveal) => {
    var windowHeight = window.innerHeight;
    var elementTop = reveal.getBoundingClientRect().top;
    var elementVisible = 100;

    if (elementTop < windowHeight - elementVisible) {
      reveal.classList.add('active');
    } else {
      reveal.classList.remove('active');
    }
  });
}

window.addEventListener("scroll", reveal);