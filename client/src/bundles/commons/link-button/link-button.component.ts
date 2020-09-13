import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-link-button',
  templateUrl: './link-button.component.html',
  styleUrls: ['./link-button.component.styl']
})
export class LinkButtonComponent implements OnInit {
  @Input() link: string;
  @Input() title: string;
  constructor() { }

  ngOnInit(): void {
  }

}
