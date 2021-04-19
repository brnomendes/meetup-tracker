import { Component, Input } from '@angular/core';
import { MeetupEvent } from 'src/app/models/meetup';

@Component({
  selector: 'events',
  templateUrl: './events.component.html',
})
export class EventsComponent {
  @Input() events: MeetupEvent[];
}
