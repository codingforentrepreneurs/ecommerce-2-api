eCommerce 2 **API** Tutorial Series
=========

eCommerce 2 API is a step-by-step guide to implementing an RESTful API into your [eCommerce 2 project](https://github.com/codingforentrepreneurs/ecommerce-2) using the Django Rest Framework, Django Rest Framework JWT, Django CORS Headers, and more. 

The project we use is [eCommerce 2](https://github.com/codingforentrepreneurs/ecommerce-2). Created by Team CFE @ [http://joincfe.com](http://joincfe.com).



## Project Overview

1. Implement a RESTful API ([wikipedia](https://en.wikipedia.org/wiki/Representational_state_transfer)) to a pre-existing eCommerce project made in Django. ([Souce Code](https://github.com/codingforentrepreneurs/ecommerce-2) | [Video Series](http://joincfe.com/projects/ecommerce-2))

2. Products & Categories
	- Create Serializers and API Views
	- Product variations API (pricing + name)
	- Implement product photos

3. Querying & Filtering
	- Create a Search Function for the API
	- Enable a Django Filter for further filtering of Search Results (or List Results)

4. User Specific
	- Cart, Checkout, & finalizing Orders
	- JWT (JSON Web Token) Authentication
	- View User-only Orders

5. Required Packages
	- Everything in `src/requirements.txt` of the [eCommerce 2 project](https://github.com/codingforentrepreneurs/ecommerce-2)
	- Django Rest Framework (for API)
	- Django Rest Framework JWT (for Auth)
	- Django CORS Headers (for cross-origin HTTP requests)


#### [API Guide](./api_guide.md)



Interested in learning more?

Sign up on our [YouTube channel](http://joincfe.com/youtube)

Become a member on [Coding for Entrepreneurs](http://joincfe.com/enroll)





The tutorial code below is the final code from the end of each tutorial video. Each link below is tied directly to the tutorial's title. Please note that some videos will not have code reference code.



## Tutorial Code


[5 - Pip Intallations](../../tree/41dc4eb252832a6e13235828c3d45a554240b410)

[6 - Model Serializers](../../tree/ba55946a1f544fe2b2b120c1cf236f1c0f3ebd88)

[7 - API List View](../../tree/e8793e5ebabe3fc309d2b94f49407ae7ba79cb8e)

[8 - API Retrieve View & URL](../../tree/dfb1e11817f856f19de1d242efb6f1aec8b55c7c)

[9 - Product & Variation Serializers](../../tree/93c6309dda6740384e3dec2e597e2a6b6577d39f)

[10 - Product List & Retrieve View](../../tree/a14a0d3f8f0d77321d3be19077626c71f4168de6)

[11 - Update & Create in the API](../../tree/2711dcea48ca3e457e7259c6f58f0e997739b47a)

[12 - Permissions](../../tree/98751539143cb866c41e43bcda980bcd15dfd2c0)

[13 - Authentication](../../tree/85addade05a099445d486391d91294d8b30e4a27)

[14 - Pagination](../../tree/f07d0895c753ebc7e4e708c4628c01d2316fa098)

[15 - Filtering the API](../../tree/7571b2656514b1c9970203fdb610b670bce327ad)

[16 - Using a Base API View](../../tree/36520cdb40b1f22282ab1af6b678270d62ddf021)

[17 - User Checkout Part 1](../../tree/3c5828d36a452431773927ea1c409ddc947d7f2d)

[18 - User Checkout Part 2](../../tree/de4f40fc0052032dc8f6bb166586c14bc78e006e)

[19 - User Checkout Part 3](../../tree/475491f3e0a08221a9b2e06d9c21c3a68252a392)

[20 - Auth with JWT Tokens](../../tree/44a974521efd507014f11c5446cf01c762342b1d)

[21 - Testing JWT Tokens with Python Requests](../../tree/6418b72838e251f763efd426e615f393973bc7ed)

[22 - JWT Token Refresh](../../tree/40d9769928a190dece439c93b85ddc488d2582c8)

[23 - Cart API View](../../tree/dd6448888389e2f82331ac7499c97b847bdaff45)

[24 - Cart Token](../../tree/3351f21d60e3485c7890b9733151f17d5b1e6e06)

[25 - Update Cart in API](../../tree/6973cae5d332e6b0e3bd5e4fee7f293ac5fd88d1)

[26 - Testing Cart API with Python Requests](../../tree/1eaa577e69ae4d7da82105616413b44ebd69bf9b)

[27 - Display Cart Items](../../tree/fb1ef3d7447afc14b2a1bd94382bb998f6c5199d)

[28 - Token Mixin](../../tree/b11ad324671f0b14e2e10fb8a7d525bb92e1307d)

[29 - Checkout API View Part 1](../../tree/d998bb123904642a1fa59c9139dd900b3f292d0e)

[30 - CartToken Mixin](../../tree/c5933309ddc99d5bc2cb0d127585a96cfde643b4)

[31 - Refactor Cart API View](../../tree/6c9a0783983c42e8c9fd20681d34e448a8fb618d)

[32 - Checkout API View Part 2](../../tree/b17555c86422582ad8ae9836516e78846285c6b3)

[33 - Order Serializer](../../tree/50a424bd74d4cd20f9fa5e27af9b43717d72cf21)

[34 - Add User to Checkout](../../tree/50a424bd74d4cd20f9fa5e27af9b43717d72cf21)

[35 - User Address Create & List](../../tree/b5f02b22ab2392a554ceb5d78d7fd159bc01ce35)

[36 - Checkout API View Part 3](../../tree/eb8bb1fe54b03f92d45df7f0b5d0776c47b94444)

[37 - Checkout API View Part 4](../../tree/eb8bb1fe54b03f92d45df7f0b5d0776c47b94444)

[38 - Custom Serializer for Checkout](../../tree/f15058d737b736fd764181c3afa8c98b45ef95d3)

[39 - Serializer Validation](../../tree/3ab5e9159835fa297063e4278916cef5c4e1c77c)

[40 - API Test Function](../../tree/79f995a27b35d54f14f596181530486cc410a362)

[41 - Order from Validated Data](../../tree/37202faebde14ab62d9b127ed878fee40cb87abf)

[42 - Finalize Order Serializer](../../tree/a9c6e98052b5d6215440be3943d18ff5953e5f8a)

[43 - Finalize Order API View](../../tree/1b24aafd0a87963588881da76b5234e7e31d0d01)

[44 - Get Client Token](../../tree/952366f1a0c174850dfa398c414d4bc8e2d7a3d9)

[API Test Index.html](../../tree/7aadc1a4447b4187af9deea57d9b5b0ac8ce01cf)

[45 - Payment Transactions](../../tree/31d120bd2008b2d266a79010cbe8c566b31381a3)

[46 - Django CORS Headers.mp4](../../tree/5b6d9de8e3f58c2c93638bc88fd3b257b8623ca0)

[47 - Order List & Retrieve](../../tree/7e8f8e04dfd8290a7d72b0bc4a3ee78316e7c54a)

[49 - Final Edits](../../tree/c4e59aa13e4682f147314637dcfb3f6d38af939d)

[50 - Final Code](../../tree/2e03047e4a58a7a51bf49a9eeff997820df1ac72)


