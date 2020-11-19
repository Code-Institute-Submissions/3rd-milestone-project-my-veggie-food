# My Veggie Food - Testing details

#### <a href="https://github.com/cotebarrientos/3rd-milestone-project-my-veggie-food/blob/master/README.md" target="_blank">Main README.md file</a>
#### <a href="https://my-veggie-food-2020recipes.herokuapp.com/" target="_blank">View Website</a>

## Testing

The testing process is outlined below. It includes:

- Validating HTML, CSS, Javascript and Python code.
- Testing website compatibility on different browsers.
- Testing responsiveness in different screen sizes.
- Manually testing the functionality of the links.
- Manually testing creating an user account.
- Manually testing proving that the user is logged in.
- Manually testing of the user profile.
- Manually testing the functionality of creating a recipe.
- Manually testing the functionality of editing a recipe.
- Testing manually the function of delete a recipe.
- Manually testing the search bar.
- Manually testing on Contact page, checking the contact form is working correctly.

## Validating HTML, CSS, Javascript and Python code.

### CSS
I checked my CSS code with the <a href="https://jigsaw.w3.org/css-validator/" target="_blank">W3C Markup Validation Service</a>. This test did not produce any error.

<img src="../testing-img/css_validation.png" alt="css validation">

## Compatibility with different browsers

In order to ensure that the website would work properly in the following browsers, responsiveness tests, button and link checks were done, as well as tests on the look of the website to ensure that the colors, images and fonts used would display correctly.

- Mozilla Firefox
- Google Chrome
- Microsoft Edge
- Apple Safari

## Responsiveness in different screen sizes

I have made the following response tests in order to ensure that the website operates correctly and at the same time that its components are seen harmoniously arranged in different screen sizes, so that I used the following tools to help me.

- **Responsinator**: This website was used to simulate different screen sizes of mobile devices. This was really useful, because it showed in real time the aspect of the tested website, helping to discover different responsiveness problems.

Here as you can see, there are some screenshots of how the website looks in different screen sizes.

<img src="../testing-img/001-mobile 1.jpg" alt="mobile 1">
<img src="../testing-img/002-mobile 2.jpg" alt="mobile 2">
<img src="../testing-img/003-mobile 3.jpg" alt="mobile 3">
<img src="../testing-img/004-mobile 4.jpg" alt="mobile 4">
<img src="../testing-img/005-mobile 5.jpg" alt="mobile 5">
<img src="../testing-img/006-mobile 6.jpg" alt="mobile 6">

- **Mozilla Firefox**: This browser was used to check the behavior of the web page in different screen sizes using the Developer Tools. Tests consisted in testing the appearance of the fonts used, the aspect of colors and backgrounds, the order and space used by the different elements that make up the web page.

- **Google Chrome**: This browser was used to check the behavior of the web page in different screen sizes using the Developer Tools. As in the previous browser, different tests were performed checking the aspect of the font used, colors and backgrounds, and finally, the space used by the elements of the website. In addition, a contrast was made between both browsers, checking for any existing differences.

- **Xiaomi Mi A1**: This mobile device was used to test the behavior of the website, using browsers such as Chrome, Mozilla Firefox and DuckDuckGo.

- **Xiaomi Poco x3**: This mobile device was used to test the behavior of the website, using browsers such as Chrome, Mozilla Firefox and DuckDuckGo.

## Manually testing the functionality of the links

The following test were made to check that all links responded as they should:

- Menu bar items were clicked on from each page to make sure that they navigate to the correct page.
- Clicking on the logo in the menu bar leads the user back to the home page.
- All buttons were clicked on to check that they take the user to the correct page.
- The registration form button is only active when all fields are completed.
- The login form button is only active when the user completes the required fields.
- The submit button is only activated if both the form to add or edit recipes is fully completed.
- The button to delete recipes is only activated if the user confirms this action in the modal window.
- The contact form "Send Message" button only accepts the form when it has completed with all required fields filled in. After that, the Send Message button opens a modal window with a successful message as expected.
- The scroll back to top button in the Analytics page works properly.

## Manually testing on Contact page

The contact form was made responsive using the EmailJS service. In order to test that the contact form works properly, I did the following tests:

1. I tried submitting the form without the **name**.

<img src="../testing-img/01-contact_form_test.jpg" alt="contact test">

2. I tried submitting the form without the **email**.

<img src="../testing-img/02-contact_form_test.jpg" alt="contact test">

3. I tried submitting the form without the **message**.

<img src="../testing-img/03-contact_form_test.jpg" alt="contact test">

As you can see, the contact form produced the correct error message as expected.

The following test consisted of filling out the entire contact form and checking that the message was indeed sent.

<img src="../testing-img/04-contact_form_test.jpg" alt="contact test">
<img src="../testing-img/05-contact_form_test.jpg" alt="contact test">

- As you can see, the message was sent correctly, and a modal window appears with a message that warns us that the message was indeed sent.

<img src="../testing-img/06-contact_form_test.jpg" alt="contact test">

- In this screenshot, you can see that the message has indeed reached the email that has been used to receive the users' messages.