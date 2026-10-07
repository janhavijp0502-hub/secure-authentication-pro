# Authentication Security Note

This project demonstrates basic defensive authentication practices.

## Security Controls

1. Passwords are stored using secure password hashing.
2. User input is validated on the server side.
3. Session cookies use HTTPOnly and SameSite settings.
4. Sessions are cleared when the user logs out.
5. Sessions have a limited lifetime.
6. Login attempts are rate-limited.
7. Generic login errors help prevent username enumeration.

## Project Purpose

This is a beginner-level cybersecurity project created to demonstrate secure authentication concepts.

## Important Note

This project is for educational purposes and should not be considered a production-ready authentication system.