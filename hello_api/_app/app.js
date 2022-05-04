import { Application } from "@hotwired/stimulus"
import { definitionsFromContext } from "@hotwired/stimulus-webpack-helpers"
//import ClipboardController from "./controllers/clipboard_controller"
import styles from "./styles/app.scss";

import * as Turbo from "@hotwired/turbo";
//var Turbolinks = require("turbolinks");
//Turbo.start();

window.Stimulus = Application.start();
//Stimulus.register("clipboard", ClipboardController)
const context = require.context("./controllers", true, /\.js$/);
Stimulus.load(definitionsFromContext(context));

// Ember exemple:
// blong: We could load stimulus controllers, turbolinks or turbo dependencies
// to improve global server-side rendering ux.
// import Ember from 'ember';
// import Resolver from './resolver';
// import loadInitializers from 'ember-load-initializers';
// import config from './config/environment';
//
// let App;
//
// Ember.MODEL_FACTORY_INJECTIONS = true;
//
// App = Ember.Application.extend({
//   modulePrefix: config.modulePrefix,
//   podModulePrefix: config.podModulePrefix,
//   Resolver
// });
//
// loadInitializers(App, config.modulePrefix);
//
// export default App;
