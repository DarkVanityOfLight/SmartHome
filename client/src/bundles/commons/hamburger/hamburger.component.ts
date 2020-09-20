import { Component, OnInit } from '@angular/core';
import { ActivateService } from 'src/services/activate.service';

@Component({
  selector: 'app-hamburger',
  templateUrl: './hamburger.component.html',
  styleUrls: ['./hamburger.component.styl']
})
export class HamburgerComponent implements OnInit {

  constructor(private activatorService: ActivateService) { }

  ngOnInit(): void {
  }

  toggleHamburger(): void{
    const hamburger = document.querySelector('.hamburger');
    hamburger.classList.toggle('checked');
    this.activatorService.toggle();
  }
}
