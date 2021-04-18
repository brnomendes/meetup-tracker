import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { MeetupGroup } from 'src/app/models/meetup';

@Component({
  selector: 'group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.scss'],
})
export class GroupComponent implements OnInit {
  @Input() group: MeetupGroup;
  @Output() showEvents: EventEmitter<number> = new EventEmitter<number>();
  constructor() {}

  ngOnInit(): void {}

  openEvents(): void {
    this.showEvents.emit(this.group.id);
  }
}
