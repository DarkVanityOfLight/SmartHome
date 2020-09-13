import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MainComponent } from './main/main.component';
import { StartComponent } from './start/start.component';



@NgModule({
  declarations: [MainComponent, StartComponent],
  imports: [
    CommonModule
  ]
})
export class SitesModule { }
