import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LinkButtonComponent } from './link-button/link-button.component';
import { RouterModule } from '@angular/router';
import { HamburgerComponent } from './hamburger/hamburger.component';



@NgModule({
  declarations: [HeaderComponent, FooterComponent, LinkButtonComponent, HamburgerComponent],
  imports: [
    CommonModule,
    RouterModule
  ],
  exports: [HeaderComponent, FooterComponent]
})
export class CommonsModule { }
