import { Injectable, EventEmitter, Output } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ActivateService {
  @Output() activated: EventEmitter<boolean> = new EventEmitter();
  constructor() { }
}
