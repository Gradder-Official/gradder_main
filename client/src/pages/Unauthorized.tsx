import React from 'react';
import { Link } from 'react-router-dom';
import StudentSidebar from '../components/StudentSidebar';


const Unauthorized = (props: any) => {

    return (
        <React.Fragment>
            
            <div className="dash-content" style={{width: "100vw", left: 0}}>
                <div className="container h-100">
                    <div className="row h-100 justify-content-center align-items-center">
                        <div className="col-12 text-center">
                            <span className="display-1 text-danger material-icons">block</span>
                            <h1 className="text-danger">No access</h1>
                            <p><em>"I'm afraid I can't do that..."</em></p>
                            <p>
                                You are not authorized to access this page.
                                Maybe go <Link to="/">home</Link>?
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </React.Fragment>
    )
  }
  
  export default Unauthorized;