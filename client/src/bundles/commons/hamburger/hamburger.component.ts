import { Component, OnInit } from '@angular/core';
import { ActivateService } from 'src/services/activate.service';

@Component({
  selector: 'app-hamburger',
  templateUrl: './hamburger.component.html',
  styleUrls: ['./hamburger.component.styl']
})
export class HamburgerComponent implements OnInit {
  public clicked: boolean;

  constructor(private activatorService: ActivateService) { }

  ngOnInit(): void {
    this.clicked = false;
  }

  toggleHamburger(): void{
    const hamburger = document.querySelector('.hamburger');
    hamburger.classList.toggle('checked');
    this.clicked = !this.clicked;
    this.activatorService.toggle();
  }
}
