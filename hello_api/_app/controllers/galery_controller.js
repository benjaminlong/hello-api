import { Controller } from "@hotwired/stimulus";


export default class extends Controller {
  static targets = [ "source" ];

  connect() {
    console.log("Galery connect");
  }

  next(event) {
    console.log(event);
    event.preventDefault();
  }
}
