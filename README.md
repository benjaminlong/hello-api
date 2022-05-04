# Welcome

This project is a Django app web-packed with 
- @hotwired/turbo
- @hotwired/stimulus
- tailwindcss

We use yarn as package manager and webpack to compile
files needed by Django server side template mechanism.

TailwindCss building process is optimized for production.

More information inside related config files:
- `postcss.config.js`
- `tailwind.config.js` 
- `webpack.*.js`
- `package.json`

### Start Django App

```
yarn install
yarn dev
yarn build
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```
