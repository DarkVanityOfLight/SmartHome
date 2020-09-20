import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LinkButtonComponent } from './link-button.component';
import { By } from '@angular/platform-browser';
import { __importStar } from 'tslib';

describe('LinkButtonComponent', () => {
  let component: LinkButtonComponent;
  let fixture: ComponentFixture<LinkButtonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LinkButtonComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(LinkButtonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display title', () => {
    component.title = 'Foo bar';
    component.link = 'foo';
    fixture.detectChanges();
    const compiled = fixture.nativeElement;
    expect(compiled.querySelector('link-button-container'));
    expect(compiled.textContent.trim()).toBe('Foo bar');
    expect(component.link).toBe('foo');
  });
});
