import { Component, OnInit } from '@angular/core';
import { ResponseDataService } from '../services/response-data.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
})
export class DashboardComponent implements OnInit {
  subjecs;

  constructor(private responseService: ResponseDataService) {}

  ngOnInit(): void {
    this.getSubjects();
  }

  getSubjects() {
    this.responseService.getSubjects().subscribe((data: any) => {
      this.subjecs = data;
      console.log(this.subjecs);
    });
  }
}
