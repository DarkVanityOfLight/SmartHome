import { Injectable, EventEmitter, Output } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ActivateService {
  visible = false
  @Output() open: EventEmitter<any> = new EventEmitter();
  @Output() close: EventEmitter<any> = new EventEmitter();
  constructor() { }

  toggle(): void{
    this.visible = !this.visible;
    if (this.visible){
      this.open.emit(null);
    }else{
      this.close.emit(null);
    }
  }
}
