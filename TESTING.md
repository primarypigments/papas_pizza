
TESTING.md 
# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

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
| Templates | 404.html | ![screenshot](documentation/validation/404.png) | |
| Templates | 500.html | ![screenshot](documentation/validation/500.png) | |
| Accounts | login.html | ![screenshot](documentation/validation/logon.png) | |
| Accounts | password_reset.html | ![screenshot](documentation/validation/forgot.png) | |
| Accounts | singup.html | ![screenshot](documentation/validation/register.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | pizza.css | ![screenshot](documentation/validation/pizza_css.png) | |
| static | index.css | ![screenshot](documentation/validation/index_css.png) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| index | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/admin.py) | ![screenshot](documentation/validation/index_admin.png) | |
| index | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/forms.py) | ![screenshot](documentation/validation/index_forms.png) | |
| index | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/models.py) | ![screenshot](documentation/validation/index_models.png) | |
| index | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/urls.py) | ![screenshot](documentation/validation/index_urls.png) | |
| index | validators.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/validators.py) | ![screenshot](documentation/validation/index_validators.png) | |
| index | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/index/views.py) | ![screenshot](documentation/validation/index_views.png) | |
|  | manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/manage.py) | ![screenshot](documentation/validation/manage.png) | |
| menu_cart | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/admin.py) | ![screenshot](documentation/validation/menu_admin.png) | |
| menu_cart | cart_context_processor.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/cart_context_processor.py) | ![screenshot](documentation/validation/menu_context.png) | |
| menu_cart | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/forms.py) | ![screenshot](documentation/validation/menu_forms.png) | |
| menu_cart | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/models.py) | ![screenshot](documentation/validation/menu_models.png) | |
| menu_cart | shell.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/shell.py) | ![screenshot](documentation/validation/menu_shell.png) | |
| menu_cart | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/urls.py) | ![screenshot](documentation/validation/menu_urls.png) | |
| menu_cart | validators.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/validators.py) | ![screenshot](documentation/validation/menu_validators.png) | |
| menu_cart | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/menu_cart/views.py) | ![screenshot](documentation/validation/menu_views.png) | |
| pizza_time | settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/pizza_time/settings.py) | ![screenshot](documentation/validation/pizza_urls.png) | |
| pizza_time | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/primarypigments/papas_pizza/main/pizza_time/urls.py) | ![screenshot](documentation/validation/pizza_settings.png) | |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Contact | Register | Sign In | Menu | Profile | Edit Menu | Cart | Success | Success Profile | 404 | Checkout | Error | Password Reset | 500 |Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| Opera | ![screenshot](documentation/browsers/opera_index.png) | ![screenshot](documentation/browsers/opera_contact.png) | ![screenshot](documentation/browsers/opera_register.png) | ![screenshot](documentation/browsers/opera_sign_in.png) | ![screenshot](documentation/browsers/opera_menu.png) | ![screenshot](documentation/browsers/opera_profile.png) | ![screenshot](documentation/browsers/opera_edit.png) | ![screenshot](documentation/browsers/opera_cart.png) | ![screenshot](documentation/browsers/opera_success.png) | ![screenshot](documentation/browsers/opera_success_profile.png) | ![screenshot](documentation/browsers/opera_404.png) | ![screenshot](documentation/browsers/opera_checkout.png) | ![screenshot](documentation/browsers/opera_error.png) | ![screenshot](documentation/browsers/opera_password_reset.png) | ![screenshot](documentation/browsers/opera_500.png) | Works as expected |
| Chrome | ![screenshot](documentation/browsers/chrome_index.png) | ![screenshot](documentation/browsers/chrome_contact.png) | ![screenshot](documentation/browsers/chrome_register.png) | ![screenshot](documentation/browsers/chrome_sign_in.png) | ![screenshot](documentation/browsers/chrome_menu.png) | ![screenshot](documentation/browsers/chrome_profile.png) | ![screenshot](documentation/browsers/chrome_edit.png) | ![screenshot](documentation/browsers/chrome_cart.png) | ![screenshot](documentation/browsers/chrome_success.png) | ![screenshot](documentation/browsers/chrome_success_profile.png) | ![screenshot](documentation/browsers/chrome_404.png) | ![screenshot](documentation/browsers/chrome_checkout.png) | ![screenshot](documentation/browsers/chrome_error.png) | ![screenshot](documentation/browsers/chrome_password_reset.png) | ![screenshot](documentation/browsers/chrome_500.png) | Works as expected |
| Brave | ![screenshot](documentation/browsers/brave_index.png) | ![screenshot](documentation/browsers/brave_contact.png) | ![screenshot](documentation/browsers/brave_register.png) | ![screenshot](documentation/browsers/brave_sign_in.png) | ![screenshot](documentation/browsers/brave_menu.png) | ![screenshot](documentation/browsers/brave_profile.png) | ![screenshot](documentation/browsers/brave_edit.png) | ![screenshot](documentation/browsers/brave_cart.png) | ![screenshot](documentation/browsers/brave_success.png) | ![screenshot](documentation/browsers/brave_success_profile.png) | ![screenshot](documentation/browsers/brave_404.png) | ![screenshot](documentation/browsers/brave_checkout.png) | ![screenshot](documentation/browsers/brave_error.png) | ![screenshot](documentation/browsers/brave_password_reset.png) | ![screenshot](documentation/browsers/brave_500.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Browser | Home | Contact | Register | Sign In | Menu | Profile | Edit Menu | Cart | Success | Success Profile | Error | 404 | Password Reset | 500 | Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |  
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/mobile_index.png) | ![screenshot](documentation/responsiveness/mobile_contact.png) | ![screenshot](documentation/responsiveness/mobile_register.png) | ![screenshot](documentation/responsiveness/mobile_signin.png) | ![screenshot](documentation/responsiveness/mobile_menu.png) | ![screenshot](documentation/responsiveness/mobile_profile.png) | ![screenshot](documentation/responsiveness/mobile_edit.png) | ![screenshot](documentation/responsiveness/mobile_checkout.png) | ![screenshot](documentation/responsiveness/mobile_success.png) | ![screenshot](documentation/responsiveness/mobile_profile_success.png)  | ![screenshot](documentation/responsiveness/mobile_error.png) | ![screenshot](documentation/responsiveness/mobile_404.png) | ![screenshot](documentation/responsiveness/mobile_forgot.png) | ![screenshot](documentation/responsiveness/mobile_500.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/tablet_index.png) | ![screenshot](documentation/responsiveness/tablet_contact.png) | ![screenshot](documentation/responsiveness/tablet_register.png) | ![screenshot](documentation/responsiveness/tablet_signin.png) | ![screenshot](documentation/responsiveness/tablet_menu.png) | ![screenshot](documentation/responsiveness/tablet_profile.png) | ![screenshot](documentation/responsiveness/tablet_edit.png) | ![screenshot](documentation/responsiveness/tablet_success.png) | ![screenshot](documentation/responsiveness/tablet_profile_success.png)  | ![screenshot](documentation/responsiveness/tablet_error.png) | ![screenshot](documentation/responsiveness/tablet_404.png) | ![screenshot](documentation/responsiveness/tablet_forgot.png) | ![screenshot](documentation/responsiveness/tablet_500.png) | Works as expected |
| Desktop | ![screenshot](documentation/browsers/opera_index.png) | ![screenshot](documentation/browsers/opera_contact.png) | ![screenshot](documentation/browsers/opera_register.png) | ![screenshot](documentation/browsers/opera_sign_in.png) | ![screenshot](documentation/browsers/opera_menu.png) | ![screenshot](documentation/browsers/opera_profile.png) | ![screenshot](documentation/browsers/opera_edit.png) | ![screenshot](documentation/browsers/opera_cart.png) | ![screenshot](documentation/browsers/opera_success.png) | ![screenshot](documentation/browsers/opera_success_profile.png)  | ![screenshot](documentation/browsers/opera_error.png) | ![screenshot](documentation/browsers/opera_404.png) | ![screenshot](documentation/browsers/opera_password_reset.png) | ![screenshot](documentation/browsers/opera_500.png) | Works as expected |


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
| 500 | ![screenshot](documentation/validation/lighthouse_500_mobile.png) | ![screenshot](documentation/validation/lighthouse_500_desktop.png) | Some minor warnings |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Contact is expected to go to contact page when the user clicks on link | Tested the feature by doing clicking on link | The feature behaved as expected, and it did go to contact page | Test concluded and passed | ![screenshot](documentation/features/footer.png) |
| | Navbar is expected to go to respective pages when the user clicks on links | Tested the feature by doing clicking on links | The feature behaved as expected, and it did go to respectivepages pages | Test concluded and passed | ![screenshot](documentation/features/navbar.png) |
| | Pizza modal link is expected to open the menu page authenticated or register unauthenticated when the user clicks on it. | Tested the feature by clicking on the link. | The feature behaved as expected and opened when clicked. | Test concluded and passed. | ![screenshot](documentation/features/index_modal.png) |
| | Social Media links are expected to open their pages when the user clicks on them | Tested the feature by doing clicking on the link | The feature behaved as expected, and opened when clicked | Test concluded and passed | ![screenshot](documentation/features/footer.png ) |
| | Cart Total is expected to  total users cart total when items are added to cart | Tested the feature by doing items are added to cart | The feature behaved as expected, and it did display cart total | Test concluded and passed | ![screenshot](documentation/features/navtotal.png) |
| Register | | | | | |
| | Number is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | Address is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | City is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | Zip Code is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | News Letter is expected to be checked if the user clicks the box | Tested the feature by clicking on the box| The feature behaved as expected, box is checked | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | Email is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | First Name is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | Last Name is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | Password1 Passowrd2 is expected to be required when the user does not not fill it out and will only accept password format | Tested the feature by leaving it blank and inouting a invalid passowrd format | The feature behaved as expected, and it give the user a message a the input is required or in enter valid format | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| | Register Button is expected to post registration of user when user clicks on the button | Tested the feature by doing clicking on button | The feature behaved as expected, and it gave success message | Test concluded and passed | ![screenshot](documentation/features/register.png) |
| Profile | | | | | |
| | Past Orders list is expected to display users Past Orders when a user clicks on the radio button | Tested the feature by clicking the on the radio button | The feature behaved as expected, and it displays Past Orders | Test concluded and passed | ![screenshot](documentation/features/profile_order.png) |
| | View Order Button expected to redirect to selected past order. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the selected past order. | Test concluded and passed | ![screenshot](documentation/features/profile_more.png) |
| Sign In | | | | | |
| | Email is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/signin.png) |
| | Sign In Button is expected when successfull redirect to index page with a success message  | Tested the feature by filling out a valid email and password and clicking the sign in button | The feature behaved as expected, and it redirected to index page with success message. | Test concluded and passed | ![screenshot](documentation/features/signin.png) |
| | Forgot Passowrd link expected to redirect to a forgot password page. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the forgot passowrd page. | Test concluded and passed | ![screenshot](documentation/features/signin.png) |
| 404 | | | | | |
| | 404 is expected to direct user to 404 page when an invalid page is entered. | Tested the feature by doing filling out  entering an invalid page. | The feature behaved as expected, and it directed to 404 page. | Test concluded and passed | ![screenshot](documentation/features/404.png) | |
| Menu | | | | | |
| | Pizza Order Modal is expected to display Pizza order options when a user clicks on the view details button | Tested the feature by clicking the on the view details button | The feature behaved as expected, and it displays pizza order options | Test concluded and passed | ![screenshot](documentation/features/menu_modal.png) |
| | Pizza Order Modal Form is expected to display Pizza toppings options, quanity and a add to cart button and add items to cart. | Tested the feature by clicking the on toppings adding more or less pizza quanity and clicking add to cart button | The feature behaved as expected, and it succfully added pizza with toppings to cart| Test concluded and passed | ![screenshot](documentation/features/menu_order.png) |
| | Add Pizza Modal is expected to display Pizza a form to add a new pizza when a user clicks on the Add New Item button | Tested the feature by clicking the on the Add new Item button | The feature behaved as expected, and it displays Add new item form | Test concluded and passed | ![screenshot](documentation/features/add.png) |
| | Edit Pizza Button expected to redirect to a Edit pizza page. | Tested the feature by clicking the button | The feature behaved as expected, and it redirected the user to the Edit pizza page. | Test concluded and passed | ![screenshot](documentation/features/menu_modal.png) |
| | Delete item Button expected to display delete item modal. | Tested the feature by clicking the button | The feature behaved as expected, and it displayed the user the Delete item modal. | Test concluded and passed | ![screenshot](documentation/features/delete.png) |
| Edit Menu | | | | | |
| | Edit Menu Form is expected to display Pizza Item options to edit (name, price, description, picture) | Tested the feature by editing a pizza item | The feature behaved as expected, and changes were saved | Test concluded and passed | ![screenshot](documentation/features/edit.png) |
| Cart | | | | | |
| | Shopping cart is expected to display Pizza Item with toppings, have the ablity to change the quanity or delete items, at bottom of cart there is a link to the menu. | Tested the feature by changeing quanity, deleting, and clicking the back to menu link | The feature behaved as expected, and quanities changed, item deleted, link direceted to menu. | Test concluded and passed | ![screenshot](documentation/features/checkout.png) |
| | Summary expected to display the total cost, the option to choose delivery or pick up, and a checkout button. | Tested the feature by choosing pick up or delivery or pick up and clicking the checkout button | The feature behaved as expected, and it displayed delivery or pick up, and the checkout button redirected to stripe checkout session. | Test concluded and passed | ![screenshot](documentation/features/checkout.png) |
| Checkout Success  | | | | | |
| |  Checkout Success is expected to display a successful order with details | Tested the feature by creating a successful order | The feature behaved as expected, and was redirected to successful checkout page | Test concluded and passed | ![screenshot](documentation/browsers/opera_success.png) |
| Checkout Success Profile | | | | | |
| |  Checkout Success is expected to display a successful order with details | Tested the feature by creating a successful order | The feature behaved as expected, and was redirected to successful checkout page | Test concluded and passed | ![screenshot](documentation/browsers/opera_success.png) |
| Contact  | | | | | |
| |  Contact form is expected to be required when the user does not not fill it out | Tested the feature by leaving it blank | The feature behaved as expected, and it give the user a message a the input is required | Test concluded and passed | ![screenshot](documentation/features/contact_empty.png) |

## Bugs

### GitHub **Issues**

**Fixed Bugs**

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3Aprimarypigments%2Fpapas_pizza%20label%3Abug&label=bugs)](https://github.com/primarypigments/papas_pizza/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

All previously closed/fixed bugs can be tracked [here](https://github.com/primarypigments/papas_pizza/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [Python `Stripe Checkout Miscalculation` ](https://github.com/primarypigments/papas_pizza/issues/17) | Closed |
| [Python `TypeError` unsupported operand type(s) for +: 'float' and 'decimal.Decimal'](https://github.com/primarypigments/papas_pizza/issues/2) | Closed |
| [Django `TemplateDoesNotExis` at index/index.html ](https://github.com/primarypigments/papas_pizza/issues/10) | Closed |
| [Django `TemplateSyntaxError` at /accounts/signup/ ](https://github.com/primarypigments/papas_pizza/issues/12) | Closed |
| [Python `Miscalculation of toppings` at index/index.html ](https://github.com/primarypigments/papas_pizza/issues/14) | Closed |
| [Python `TemplateDoesNotExis` at index/index.html ](https://github.com/primarypigments/papas_pizza/issues/10) | Closed |
| [Python `AttributeError` object has no attribute 'try_save' ](https://github.com/primarypigments/papas_pizza/issues/13) | Closed |
| [Python `DisallowedHost` Invalid HTTP_HOST header: '8000-primarypigme-papaspizza-qedyxbyhnxl.ws-eu110.gitpod.io' ](https://github.com/primarypigments/papas_pizza/issues/11) | Closed |
| [Python `AttributeError` object has no attribute 'try_save' ](https://github.com/primarypigments/papas_pizza/issues/13) | Closed |

**Open Issues**

[![GitHub issues](https://img.shields.io/github/issues/primarypigments/papas_pizza)](https://github.com/primarypigments/papas_pizza/issues)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/primarypigments/papas_pizza)](https://github.com/primarypigments/papas_pizza/issues?q=is%3Aissue+is%3Aclosed)

Any remaining open issues can be tracked [here](https://github.com/primarypigments/papas_pizza/issues).

## Unfixed Bugs
 
> There are no remaining bugs that I am aware of.