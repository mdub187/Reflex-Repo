 
# Title
 Reflex-Repo

# Description
 Template web-application project utilizing the Reflex framework, built in Python.

# Title
  Reflex-Repo
# Desription
  Template web-application project utitilizing reflex framework, built in python.
# Install
<<<<<<< HEAD
<<<<<<< HEAD
 1. Create a virtual environment:
   """ python3 -m venv .venv """
 2. Activate the environment:
   """ source .venv/bin/activate """
 3. Install dependencies:
   """ pip install -r requirements.txt """
 4. Run Reflex:
   """ reflex run """

# Environment (Auth & Development)
 This project integrates with Clerk for authentication in production via the
 `CLERK_SECRET_KEY` environment variable. For local development the UI includes
 demo login buttons that use simulated tokens (for example `demo-token` and
 `demo-admin-token`).

 - Production:
   - Set `CLERK_SECRET_KEY` to your Clerk secret so server-side token verification works.
     Example:
       export CLERK_SECRET_KEY="sk_live_..."

 - Local development (optional):
   - To enable the development fallback that accepts demo tokens when
     `CLERK_SECRET_KEY` is not set, set:
       export ALLOW_DEMO_TOKENS=true
   - When `ALLOW_DEMO_TOKENS` is enabled and `CLERK_SECRET_KEY` is not present,
     demo tokens starting with `demo` (e.g., `demo-token`, `demo-admin-token`)
     will return a lightweight demo user so you can exercise protected UI flows
     without a Clerk account.

 Security note:
   - Do NOT enable `ALLOW_DEMO_TOKENS` in production or CI. The demo fallback is
     strictly for local development convenience. In production you must set
     `CLERK_SECRET_KEY` and disable demo tokens.

=======
  1. Create virtual environment:
    """ python3 -m venv .venv """
  2. Activate Said Environment:
    """ source .venv/bin/activate """
  3. Install dependencies:
    """ pip install -r requirements.txt """
  4. run reflex:
    """ reflex run """
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
# Usage
 Extensive portfolio / e-commerce web app using only Python and Reflex libraries.

# Contribution
 Working on getting the regex for the auth login, and the redirect.
 Contributions and suggestions are welcome.

# Testing
<<<<<<< HEAD
 TBD

# License
 undefined

=======
  undefined
# Usage
  Simple web app
# Contribution
  any
# Testing
  n/a
# Liscense
  undefined
>>>>>>> origin/revert-2-new
=======
  TBD
# Liscense
  undefined
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
# Github Username
 mdub187

# Email
 maweeks.91@gmail.com
#
