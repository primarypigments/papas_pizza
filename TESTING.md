
TESTING.md 
# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section, you need to convince the assessors that you have conducted enough testing to legitimately believe that the site works well.
Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended,
with the project providing an easy and straightforward way for the users to achieve their goals.

Feature-by-Feature Testing:

Go through each feature of your portfolio site and detail the testing process for each.

Explain the functionality and demonstrate how it aligns with the intended purpose. This could include:

- Navigation: Ensuring smooth transitions between pages, links directing to the correct destinations.
- Responsive Design: Checking for compatibility across various devices and screen sizes.
- Portfolio Display: Verifying that projects are properly showcased with accurate descriptions, images, and links.
- Contact Form: Testing the form submission process, ensuring the user receives a confirmation, and you receive the message.

User Experience Testing:

- Usability Testing: Have users (or simulated users) interact with the site and provide feedback. Document any issues encountered and the resolutions implemented.
- Accessibility Testing: Confirm compliance with accessibility standards (e.g., screen reader compatibility, proper alt text for images, keyboard navigation).

Compatibility Testing:

- Browser Compatibility: Testing on different browsers (Chrome, Firefox, Safari, Edge, etc.) to ensure consistent performance.
- Device Compatibility: Ensuring functionality across various devices (desktops, laptops, tablets, and mobile phones).
- Performance Testing (optional):
	- Speed and Load Testing: Tools like PageSpeed Insights or GTmetrix to check page load times and optimize where necessary.
	- Scalability Testing: Assess how the site handles increased traffic or usage.

Regression Testing:

After implementing fixes or updates, ensure that previous features and functionalities still work as intended. This prevents new changes from breaking existing features.

Documentation and Logs:

Maintain records of testing procedures, results, and any bugs encountered along with their resolutions. This helps demonstrate a systematic approach to testing and problem-solving.
User Feedback Incorporation:

If applicable, mention how user feedback has been taken into account and implemented to enhance the user experience.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Code Validation

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use the space to discuss code validation for any of your own code files (where applicable).
You are not required to validate external libraries/frameworks, such as imported Bootstrap, Materialize, Font Awesome, etc.

**IMPORTANT**: You must provide a screenshot for each file you validate.

**PRO TIP**: Always validate the live site pages, not your local code. There could be subtle/hidden differences.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| Index | index.html | ![screenshot](documentation/validation/index.png) | |
| Cart | cart.html | ![screenshot](documentation/validation/cart.png) | |
| Checkout | error.html | ![screenshot](documentation/validation/error.png) | |
| Checkout | success.html | ![screenshot](documentation/validation/success.png) | |
| Checkout | success_profile.html | ![screenshot](documentation/validation/success_profile.png) | |
| Contact | contact.html | ![screenshot](documentation/validation/contact.png) | |
| Menu | menu.html | ![screenshot](documentation/validation/menu.png) | |
| Menu | edit_menu.html | ![screenshot](documentation/validation/edit_menu.png) | |
| Profile | profile.html | ![screenshot](documentation/validation/profile.png) | |
| Templates | 404.html | ![screenshot](documentation/validation/logout.png) | |
| Accounts | login.html | ![screenshot](documentation/validation/logon.png) | |
| Accounts | password_reset.html | ![screenshot](documentation/validation/forgot.png) | |
| Accounts | singup.html | ![screenshot](documentation/validation/register.png) | |
### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | pizza.css | ![screenshot](documentation/validation/path-to-screenshot.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| index | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| index | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/forms.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| index | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| index | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| index | validators.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/validators.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| index | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/manage.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| menu_cart | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/admin.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| menu_cart | cart_context_processor.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/cart_context_processor.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| menu_cart | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/forms.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| menu_cart | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/models.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| menu_cart | shell.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/shell.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| menu_cart | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| menu_cart | validators.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/validators.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| menu_cart | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/views.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| pizza_time | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/pizza_time/settings.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |
| pizza_time | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/pizza_time/urls.py) | ![screenshot](documentation/validation/path-to-screenshot.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Contact | Register | Sign In | Menu | Profile | Edit Menu | Cart | Success | Success Profile | 404 | Checkout | Error | Password Reset | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Opera | ![screenshot](documentation/browsers/opera_index.png) | ![screenshot](documentation/browsers/opera_contact.png) | ![screenshot](documentation/browsers/opera_register.png) | ![screenshot](documentation/browsers/opera_sign_in.png) | ![screenshot](documentation/browsers/opera_menu.png) | ![screenshot](documentation/browsers/opera_profile.png) | ![screenshot](documentation/browsers/opera_edit.png) | ![screenshot](documentation/browsers/opera_cart.png) | ![screenshot](documentation/browsers/opera_success.png) | ![screenshot](documentation/browsers/opera_success_profile.png) | ![screenshot](documentation/browsers/opera_404.png) | ![screenshot](documentation/browsers/opera_checkout.png) | ![screenshot](documentation/browsers/opera_error.png) | ![screenshot](documentation/browsers/opera_password_reset.png) | Works as expected |
| Chrome | ![screenshot](documentation/browsers/chrome_index.png) | ![screenshot](documentation/browsers/chrome_contact.png) | ![screenshot](documentation/browsers/chrome_register.png) | ![screenshot](documentation/browsers/chrome_sign_in.png) | ![screenshot](documentation/browsers/chrome_menu.png) | ![screenshot](documentation/browsers/chrome_profile.png) | ![screenshot](documentation/browsers/chrome_edit.png) | ![screenshot](documentation/browsers/chrome_cart.png) | ![screenshot](documentation/browsers/chrome_success.png) | ![screenshot](documentation/browsers/chrome_success_profile.png) | ![screenshot](documentation/browsers/chrome_404.png) | ![screenshot](documentation/browsers/chrome_checkout.png) | ![screenshot](documentation/browsers/chrome_error.png) | ![screenshot](documentation/browsers/chrome_password_reset.png) | Works as expected |
| Brave | ![screenshot](documentation/browsers/brave_index.png) | ![screenshot](documentation/browsers/brave_contact.png) | ![screenshot](documentation/browsers/brave_register.png) | ![screenshot](documentation/browsers/brave_sign_in.png) | ![screenshot](documentation/browsers/brave_menu.png) | ![screenshot](documentation/browsers/brave_profile.png) | ![screenshot](documentation/browsers/brave_edit.png) | ![screenshot](documentation/browsers/brave_cart.png) | ![screenshot](documentation/browsers/brave_success.png) | ![screenshot](documentation/browsers/brave_success_profile.png) | ![screenshot](documentation/browsers/brave_404.png) | ![screenshot](documentation/browsers/brave_checkout.png) | ![screenshot](documentation/browsers/brave_error.png) | ![screenshot](documentation/browsers/brave_password_reset.png) | Works as expected |
Use this space to discuss testing the live/deployed site on various device sizes.

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Browser | Home | Contact | Register | Sign In | Menu | Profile | Edit Menu | Cart | Success | Success Profile | 404 | Checkout | Error | Password Reset | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mobile_index.png) | ![screenshot](documentation/responsiveness/mobile_contact.png) | ![screenshot](documentation/responsiveness/mobile_register.png) | ![screenshot](documentation/responsiveness/mobile_signin.png) | ![screenshot](documentation/responsiveness/mobile_reservation.png) | ![screenshot](documentation/responsiveness/mobile_profile.png) | ![screenshot](documentation/responsiveness/mobile_edit.png) | ![screenshot](documentation/responsiveness/mobile_cancel.png) | ![screenshot](documentation/responsiveness/mobile_delete.png)  | ![screenshot](documentation/responsiveness/mobile_signout.png) | ![screenshot](documentation/responsiveness/mobile_404.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet_index.png) | ![screenshot](documentation/responsiveness/tablet_contact.png) | ![screenshot](documentation/responsiveness/tablet_register.png) | ![screenshot](documentation/responsiveness/tablet_signin.png) | ![screenshot](documentation/responsiveness/tablet_reservation.png) | ![screenshot](documentation/responsiveness/tablet_profile.png) | ![screenshot](documentation/responsiveness/tablet_edit.png) | ![screenshot](documentation/responsiveness/tablet_cancel.png) | ![screenshot](documentation/responsiveness/tablet_delete.png)  | ![screenshot](documentation/responsiveness/tablet_signout.png) | ![screenshot](documentation/responsiveness/tablet_404.png)  | Works as expected |
| Desktop | ![screenshot](documentation/browsers/opera_index.png) | ![screenshot](documentation/browsers/opera_contact.png) | ![screenshot](documentation/browsers/opera_register.png) | ![screenshot](documentation/browsers/opera_sign_in.png) | ![screenshot](documentation/browsers/opera_reservation.png) | ![screenshot](documentation/browsers/opera_profile.png) | ![screenshot](documentation/browsers/opera_edit.png) | ![screenshot](documentation/browsers/opera_cancel.png) | ![screenshot](documentation/browsers/opera_delete.png)  | ![screenshot](documentation/browsers/opera_sign_out.png) | ![screenshot](documentation/browsers/opera_404.png) | Works as expected |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/validation/lighthouse_index_mobile.png) | ![screenshot](documentation/validation/lighthouse_index_desktop.png) | Some minor warnings |
| Contact | ![screenshot](documentation/validation/lighthouse_contact_mobile.png) | ![screenshot](documentation/validation/lighthouse_contact_desktop.png) | Some minor warnings |
| Register | ![screenshot](documentation/validation/lighthouse_register_mobile.png) | ![screenshot](documentation/validation/lighthouse_register_desktop.png) | Some minor warnings |
| Sign In | ![screenshot](documentation/validation/lighthouse_signin_mobile.png) | ![screenshot](documentation/validation/lighthouse_signin_desktop.png) | Some minor warnings |
| Menu | ![screenshot](documentation/validation/lighthouse_menu_mobile.png) | ![screenshot](documentation/validation/lighthouse_menu_desktop.png) | Some minor warnings |
| Profile | ![screenshot](documentation/validation/lighthouse_profile_mobile.png) | ![screenshot](documentation/validation/lighthouse_profile_desktop.png) | Slow response time due to large images |
| Edit | ![screenshot](documentation/validation/lighthouse_edit_mobile.png) | ![screenshot](documentation/validation/lighthouse_edit_desktop.png) | Some minor warnings |
| Success | ![screenshot](documentation/validation/lighthouse_success_mobile.png) | ![screenshot](documentation/validation/lighthouse_success_desktop.png) | Some minor warnings |
| Success Profile | ![screenshot](documentation/validation/lighthouse_success_profile_mobile.png) | ![screenshot](documentation/validation/lighthouse_success_profile_desktop.png) | Some minor warnings |
| Forgot Password | ![screenshot](documentation/validation/lighthouse_forgot_mobile.png) | ![screenshot](documentation/validation/lighthouse_forgot_desktop.png) | Some minor warnings |
| Cart | ![screenshot](documentation/validation/lighthouse_cart_mobile.png) | ![screenshot](documentation/validation/lighthouse_cart_desktop.png) | Some minor warnings |
| Checkout | ![screenshot](documentation/validation/lighthouse_checkout_mobile.png) | ![screenshot](documentation/validation/lighthouse_checkout_desktop.png) | Some minor warnings |
| Error | ![screenshot](documentation/validation/lighthouse_error_mobile.png) | ![screenshot](documentation/validation/lighthouse_error_desktop.png) | Some minor warnings |
| 404 | ![screenshot](documentation/validation/lighthouse_404_mobile.png) | ![screenshot](documentation/validation/lighthouse_404_desktop.png) | Some minor warnings |


## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I can select a pick-up option, so that I can collect my order from the restaurant at my convenience. | ![screenshot](documentation/features/feature01.png) |
|  As a new site user, I can view the detailed menu with toppings and prices on the website, so that I can choose my meals according to my preference and budget.. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I can create a user account on the website, so that I can save my preferences and order history for future orders. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to review my past orders, so that I can order the same pizzas. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to view my past orders, so that I can easily see a previous order or use it as a starting point for a new customization. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to have access to reset my password, so that I can login to my account. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to reset user passwords upon request, so that I can provide support for account access issues. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/primarypigments/papas_pizza/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aprimarypigments%2Fpapas_pizza%20label%3Abug&label=bugs)](https://github.com/primarypigments/papas_pizza/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/primarypigments/papas_pizza/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/primarypigments/papas_pizza/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/primarypigments/papas_pizza/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/primarypigments/papas_pizza/issues/3) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/primarypigments/papas_pizza)](https://github.com/primarypigments/papas_pizza/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/primarypigments/papas_pizza)](https://github.com/primarypigments/papas_pizza/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/primarypigments/papas_pizza/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/primarypigments/papas_pizza/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/primarypigments/papas_pizza/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.