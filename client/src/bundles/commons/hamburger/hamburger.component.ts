import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hamburger',
  templateUrl: './hamburger.component.html',
  styleUrls: ['./hamburger.component.styl']
})
export class HamburgerComponent implements OnInit {
  public clicked: boolean;

  constructor() { }

  ngOnInit(): void {
    this.clicked = false;
  }

  toggleHamburger(): void{
    const hamburger = document.querySelector('.hamburger');
    hamburger.classList.toggle('checked');
    this.clicked = !this.clicked;
  }
}
