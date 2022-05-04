import { Controller } from "@hotwired/stimulus";


export default class extends Controller {
  static targets = [ "source" ];

  connect() {
    console.log("Clipboard Connect");
  }

  copy(event) {
    console.log("Copied");
    event.preventDefault();
    this.sourceTarget.select();
    document.execCommand("copy");
  }
}
