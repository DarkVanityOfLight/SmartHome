import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-hamburger',
  templateUrl: './hamburger.component.html',
  styleUrls: ['./hamburger.component.styl']
})
export class HamburgerComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  toggleHamburger(): void{
    const hamburger = document.querySelector('.hamburger');
    hamburger.classList.toggle('checked');
  }
}
