import { Component, OnInit } from '@angular/core';
import { MeetupEvent, MeetupGroup } from 'src/app/models/meetup';
import { GroupService } from 'src/app/services/group.service';

@Component({
  selector: 'workspace',
  templateUrl: './workspace.component.html',
  styleUrls: ['./workspace.component.scss'],
})
export class WorkspaceComponent implements OnInit {
  groups: MeetupGroup[] = [];
  displayEvents: boolean = false;
  currentGroupId: number = undefined;
  currentEvents: MeetupEvent[] = [];

  constructor(private groupService: GroupService) {}

  ngOnInit(): void {
    this.getGroups();
  }

  showEvents(groupId: number): void {
    this.groupService.getEvents(groupId).subscribe((events: MeetupEvent[]) => {
      this.currentEvents = events;
      this.currentGroupId = groupId;
      this.displayEvents = true;
    });
  }

  updateGroup(groupId: number): void {
    this.groupService.updateGroup(groupId).subscribe((g) => {
      this.getGroups();
      if (this.displayEvents && this.currentGroupId == groupId)
        this.showEvents(groupId);
    });
  }

  getGroups(): void {
    this.groupService
      .getGroups()
      .subscribe((g: MeetupGroup[]) => (this.groups = g));
  }
}
