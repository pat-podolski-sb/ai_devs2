Solution:

1. Register on RenderForm website https://renderform.io/
2. Create new Template there
  - remember ID of this template. You will use it in the API
  - template should have black background (just fill rectangle with black color)
  - there should be huge image container in the center (give it a simple 'NAME')
  - put text container under the image, and set color to white (also, give container a NAME!)
  - save your template
3. Use API or module inside Make to create new image. You have to send some extra variables
  - here is API documentation: https://renderform.io/docs/api/get-started/
  - for Make, you don't need any doc. It's just click & play
  - you will get meme image and text directly from /task/ endpoint
4. Send image URL (RenderForm will provide it to you) and send it to /answer/
{
 "answer":"	https://cdn.renderform.io/...................jpg"
}


____________

Some additional tips:

- to change text on the template, use property "NAME.text"
- to change source of the image, use property "NAME.src"