import { Component, OnInit } from '@angular/core';
import { ActivateService } from 'src/services/activate.service';

@Component({
  selector: 'app-overlay',
  templateUrl: './overlay.component.html',
  styleUrls: ['./overlay.component.styl']
})
export class OverlayComponent implements OnInit {
  public isHidden: boolean;

  constructor(private activator: ActivateService) {
    activator.close.subscribe(() => {
      this.isHidden = true;
    });
    activator.open.subscribe(() => {
      this.isHidden = false;
    }
    );
  }

  ngOnInit(): void {
    this.isHidden = true;
  }

}
