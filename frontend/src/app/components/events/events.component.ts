import { Component, Input } from '@angular/core';
import { MeetupEvent } from 'src/app/models/meetup';

@Component({
  selector: 'events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.scss'],
})
export class EventsComponent {
  @Input() events: MeetupEvent[];

  goToLink(url: string): void {
    window.open(url, '_blank');
  }
}
