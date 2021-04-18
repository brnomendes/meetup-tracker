import { Component, Input, OnInit } from '@angular/core';
import { MeetupGroup } from 'src/app/models/meetup';

@Component({
  selector: 'group',
  templateUrl: './group.component.html',
  styleUrls: ['./group.component.scss'],
})
export class GroupComponent implements OnInit {
  @Input() group: MeetupGroup;
  constructor() {}

  ngOnInit(): void {}
}
