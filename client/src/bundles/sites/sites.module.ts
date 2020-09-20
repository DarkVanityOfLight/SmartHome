import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StartComponent } from './start/start.component';
import { OverlayComponent } from './overlay/overlay.component';



@NgModule({
  declarations: [StartComponent, OverlayComponent],
  imports: [
    CommonModule
  ],
  exports: [StartComponent]
})
export class SitesModule { }
