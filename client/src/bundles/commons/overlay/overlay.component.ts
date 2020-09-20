import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-overlay',
  templateUrl: './overlay.component.html',
  styleUrls: ['./overlay.component.styl']
})
export class OverlayComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    const burger = document.querySelector('.hamburger');
    const site = document.querySelector('.app');
  }

}
