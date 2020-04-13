import React, {Component} from 'react';
import Grid from '@material-ui/core/Grid';
import TextField from '@material-ui/core/TextField';
import TransactionsTable from '../TransactionsTable/TransactionsTable';
import SimpleHeader from '../Header/Header';
import SimplePaper from '../Paper/Paper';


export default class App extends Component {  
	render() {
		return (
			<Grid container>
				<Grid item xs={12}>
					<SimpleHeader></SimpleHeader>
				</Grid>
        <Grid item xs={6}>
      		<TransactionsTable></TransactionsTable>
        </Grid>
        <Grid item xs={3}>
          <SimplePaper>
            <form className='& .MuiTextField-root' noValidate autoComplete="off">
              <div>
                <TextField label="Number" type="number"></TextField>
              </div>
            </form>
          </SimplePaper>
        </Grid>
        <Grid item xs={3}>
          <SimplePaper></SimplePaper>
        </Grid>
			</Grid>
		);
	}
}
