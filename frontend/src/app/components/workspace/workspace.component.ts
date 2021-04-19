import { Component, OnInit, ViewChild } from '@angular/core';
import { MessageService } from 'primeng/api';
import { City, MeetupEvent, MeetupGroup } from 'src/app/models/meetup';
import { GroupService } from 'src/app/services/group.service';

@Component({
  selector: 'workspace',
  templateUrl: './workspace.component.html',
  styleUrls: ['./workspace.component.scss'],
})
export class WorkspaceComponent implements OnInit {
  groups: MeetupGroup[] = [];
  displayEvents: boolean = false;
  currentEvents: MeetupEvent[] = [];
  currentEventsGroup: MeetupGroup;

  constructor(
    private groupService: GroupService,
    private messageService: MessageService
  ) {}

  ngOnInit(): void {
    this.getGroups();
  }

  showEvents(group: MeetupGroup): void {
    this.groupService.getEvents(group.id).subscribe((events: MeetupEvent[]) => {
      this.currentEventsGroup = group;
      this.currentEvents = events;
      this.currentEvents.sort((a, b) => b.time - a.time);
      this.displayEvents = true;
    });
  }

  updateGroup(group: MeetupGroup): void {
    this.groupService.updateGroup(group.id).subscribe(
      (g) => {
        this.getGroups();
        this.messageService.add({
          severity: 'success',
          summary: 'Success',
          detail: `Group ${group.name} data successfully synchronized with meetup.com`,
        });
      },
      () => {
        this.messageService.add({
          severity: 'error',
          summary: 'Error',
          detail: `Failed to synchronize group ${group.name} data with meetup.com`,
        });
      }
    );
  }

  getGroups(): void {
    this.groupService
      .getGroups()
      .subscribe((g: MeetupGroup[]) => (this.groups = g));
  }
}
