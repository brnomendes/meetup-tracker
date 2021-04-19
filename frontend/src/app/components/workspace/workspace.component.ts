import { Component, OnInit } from '@angular/core';
import { NgxSpinnerService } from 'ngx-spinner';
import { MessageService } from 'primeng/api';
import { MeetupEvent, MeetupGroup } from 'src/app/models/meetup';
import { GroupService } from 'src/app/services/group.service';

@Component({
  selector: 'workspace',
  templateUrl: './workspace.component.html',
})
export class WorkspaceComponent implements OnInit {
  groups: MeetupGroup[] = [];
  displayEvents: boolean = false;
  currentEvents: MeetupEvent[] = [];
  currentEventsGroup: MeetupGroup;

  constructor(
    private groupService: GroupService,
    private messageService: MessageService,
    private spinner: NgxSpinnerService
  ) {}

  ngOnInit(): void {
    this.spinner.show();
    this.getGroups();
  }

  showEvents(group: MeetupGroup): void {
    this.groupService.getEvents(group.id).subscribe(
      (events: MeetupEvent[]) => {
        this.currentEventsGroup = group;
        this.currentEvents = events;
        this.currentEvents.sort((a, b) => b.time - a.time);
        this.displayEvents = true;
      },
      () => {
        this.messageService.add({
          severity: 'error',
          summary: 'Error',
          detail: `Failed to load events of group ${group.name}`,
        });
      }
    );
  }

  updateGroup(group: MeetupGroup): void {
    this.spinner.show();
    this.groupService.updateGroup(group.id).subscribe(
      () => {
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
        this.spinner.hide();
      }
    );
  }

  getGroups(): void {
    this.groupService.getGroups().subscribe(
      (g: MeetupGroup[]) => {
        this.groups = g;
        this.spinner.hide();
      },
      () => {
        this.messageService.add({
          severity: 'error',
          summary: 'Error',
          detail: 'Failed to load groups data',
        });
        this.spinner.hide();
      }
    );
  }
}
