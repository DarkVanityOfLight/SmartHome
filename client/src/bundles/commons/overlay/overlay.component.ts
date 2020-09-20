import { Component, OnInit } from '@angular/core';
import { ActivateService } from 'src/services/activate.service';

@Component({
  selector: 'app-overlay',
  templateUrl: './overlay.component.html',
  styleUrls: ['./overlay.component.styl']
})
export class OverlayComponent implements OnInit {
  isHidden: boolean;

  constructor(private activator: ActivateService) {
    activator.close.subscribe(this.hide());
    activator.open.subscribe(this.show());
  }

  ngOnInit(): void {
    const burger = document.querySelector('.hamburger');
    const site = document.querySelector('.app');
  }

  show(): void {
    this.isHidden = false;
  }

  hide(): void {
    this.isHidden = true;
  }

}
