import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LinkButtonComponent } from './link-button/link-button.component';



@NgModule({
  declarations: [HeaderComponent, FooterComponent, LinkButtonComponent],
  imports: [
    CommonModule
  ],
  exports: [HeaderComponent, FooterComponent]
})
export class CommonsModule { }
