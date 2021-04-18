import { Component, OnInit } from '@angular/core';
import { MeetupGroup } from 'src/app/models/meetup';
import { GroupService } from 'src/app/services/group.service';

@Component({
  selector: 'workspace',
  templateUrl: './workspace.component.html',
  styleUrls: ['./workspace.component.scss'],
})
export class WorkspaceComponent implements OnInit {
  groups: MeetupGroup[] = [];

  constructor(private groupService: GroupService) {}

  ngOnInit(): void {
    this.groupService.getGroups().subscribe((g) => (this.groups = g));
  }
}
