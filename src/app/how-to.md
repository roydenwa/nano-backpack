## build dockerimage with:
`docker build -t "nano-backpack" .`

## start dockerimage with:
`docker run --rm -it -p 80:80 nano-backpack`

## start development server without docker:
`python app.py`

## Nice to know:
* app should run at http://localhost:80

* manual restart of app after changes to UI5-frontend required, b/c auto-reload
  only covers changes in python code.

* disable browser-caching not working for Chrome --> use Edge or Firefox for dev
