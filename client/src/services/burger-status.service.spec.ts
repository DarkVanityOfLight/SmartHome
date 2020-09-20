import { TestBed } from '@angular/core/testing';

import { BurgerStatusService } from './burger-status.service';

describe('BurgerStatusService', () => {
  let service: BurgerStatusService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BurgerStatusService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
