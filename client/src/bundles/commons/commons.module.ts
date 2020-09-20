import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LinkButtonComponent } from './link-button/link-button.component';
import { RouterModule } from '@angular/router';
import { HamburgerComponent } from './hamburger/hamburger.component';
import { OverlayComponent } from './overlay/overlay.component';



@NgModule({
  declarations: [HeaderComponent, FooterComponent, LinkButtonComponent, HamburgerComponent, OverlayComponent],
  imports: [
    CommonModule,
    RouterModule
  ],
  exports: [HeaderComponent, FooterComponent, OverlayComponent]
})
export class CommonsModule { }
