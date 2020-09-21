import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { StartComponent } from './start/start.component';
import { GarageComponent } from './garage/garage.component';



@NgModule({
  declarations: [StartComponent, GarageComponent],
  imports: [
    CommonModule
  ],
  exports: [StartComponent]
})
export class SitesModule { }
