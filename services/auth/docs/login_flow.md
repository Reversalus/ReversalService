### OTP-Based Login Flow
> (For users logging in with a phone number and OTP)

- User enters phone number & requests OTP
- DB Call: Check if the phone number exists in users table
    - If exists → Proceed to OTP verification
    - If not exists → Move to Step 2

> Send OTP to phone

- Generate and send OTP via SMS.
- Store the OTP temporarily in a cache (e.g., Redis) or in an otp_verifications table with an expiration time.

> User enters OTP for verification

- DB Call: Check the OTP from cache/table
    - If OTP is correct → Proceed to Step 4
    - If OTP is incorrect/expired → Reject request

> Check if the user exists

- If user already exists, update auth_phone = true (if not already set) and log them in.
- If user does not exist, proceed to user details collection (Step 5).

> (For new users) Show user details input screen

- User fills in first_name, last_name, etc.

> Create a new user record in the database

- DB Call: Insert user into users table
    ```sql
    INSERT INTO users (first_name, last_name, phone, auth_phone) 
    VALUES (<user details>, true);
    ```

Log the user in.


### Google-Based Login Flow
> (For users logging in via Google)

> User clicks "Sign in with Google"

- Frontend gets Google OAuth token & user info.

> Frontend sends Google token to backend

- Backend verifies the token using Google's OAuth API.
- Extracts user details (first_name, last_name, email, profile_image_uri).

> Check if the user exists in the database

- DB Call: Find user by email
    ```sql
    SELECT * FROM users WHERE email = '<google_email>';
    ```
- If user exists → Update auth_google = true if not already set.
- If user does not exist, move to Step 4.

> Ask user for phone number (for new users)

- If phone number is already in DB, associate it with this user.
- If not, send OTP for phone verification.

> User enters OTP for phone verification

- Same OTP process as in OTP login above (Step 3).

> Create new user record in the database (if new user)

- DB Call: Insert user into users table
    ```sql
    INSERT INTO users (first_name, last_name, email, phone, profile_image_uri, auth_google, auth_phone) 
    VALUES (<user details>, true, true);
    ```
- Log the user in.


Summary of Database Calls
Step	Action	DB Call
OTP Login		
1	Check if phone exists	SELECT * FROM users WHERE phone = '<phone>';
3	Verify OTP	Check OTP cache/table
4	Update auth_phone	UPDATE users SET auth_phone = true WHERE phone = '<phone>';
6	Insert new user	INSERT INTO users (...) VALUES (...);
Google Login		
3	Check if email exists	SELECT * FROM users WHERE email = '<google_email>';
4	Check phone number	SELECT * FROM users WHERE phone = '<phone>';
6	Insert new user	INSERT INTO users (...) VALUES (...);