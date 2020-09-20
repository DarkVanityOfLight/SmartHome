import { Injectable, EventEmitter, Output } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class BurgerStatusService {
  @Output() ClickedEvent: EventEmitter<boolean> = new EventEmitter();
  constructor() { }
}
