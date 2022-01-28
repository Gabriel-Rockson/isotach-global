let current_img = 1
displayImg(current_img)

function nextImg(n) {
  displayImg(current_img += n)
}

function currentSlide(n) {
  displayImg(current_img = n)
}

function displayImg(image_no) {
  let images = document.querySelectorAll('.slide')
  let dots = document.querySelectorAll('.dot')

  for (let i = 0; i < images.length; i++) {
    images[i].style.display = 'none'
  }

  for (let i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "")
  }

  if (image_no > images.length) {
    current_img = 1
  }

  if (image_no < 1) {
    current_img = images.length
  }

  images[current_img - 1].style.display = 'block'
  dots[current_img - 1].className += ' active'
}