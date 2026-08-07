"""
Main Application Entry Point
AI Construction Site Safety Intelligence Platform

This script integrates all modules and provides the main entry point for the application.
"""

import sys
import argparse
from pathlib import Path
import logging
import subprocess

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))

from src.detection import SafetyDetector
from src.tracking import ObjectTracker
from src.analytics import SafetyAnalytics
from src.alerts import AlertSystem
from src.risk import RiskEngine
from src.reporting import ReportGenerator

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SafetyPlatform:
    """Main class for the AI Construction Site Safety Platform"""
    
    def __init__(self, model_path: str = None,
                 device: str = 'cuda:0'):
        """
        Initialize the safety platform
        
        Args:
            model_path (str): Path to trained YOLOv8 model
            device (str): Device to use for inference
        """
        if model_path is None:
            model_path = str(Path(__file__).resolve().parent / 'models' / 'safety_detection' / 'weights' / 'best.pt')
        self.model_path = model_path
        self.device = device
        
        # Initialize components
        logger.info("Initializing Safety Platform components...")
        self.detector = SafetyDetector(model_path=model_path, device=device)
        self.tracker = ObjectTracker()
        self.analytics = SafetyAnalytics()
        self.alert_system = AlertSystem()
        self.risk_engine = RiskEngine()
        self.report_generator = ReportGenerator()
        
        logger.info("Safety Platform initialized successfully")
        
    def run_detection(self, video_source: int = 0, output_path: str = None):
        """
        Run real-time detection on video stream
        
        Args:
            video_source: Video source (webcam index, video file path, or RTSP stream)
            output_path (str): Path to save output video (optional)
        """
        logger.info(f"Starting detection on source: {video_source}")
        self.detector.detect_video(video_source=video_source, output_path=output_path)
        
    def run_dashboard(self):
        """Launch the Streamlit dashboard"""
        logger.info("Launching Streamlit dashboard...")
        
        # Run Streamlit app
        dashboard_path = Path(__file__).parent / 'dashboard' / 'app.py'
        subprocess.run(['streamlit', 'run', str(dashboard_path)])
        
    def run_detection_with_tracking(self, video_source: int = 0):
        """
        Run detection with object tracking enabled
        
        Args:
            video_source: Video source
        """
        logger.info(f"Starting detection with tracking on source: {video_source}")
        
        # This would integrate detection and tracking
        # For now, run basic detection
        self.detector.detect_video(video_source=video_source)
        
    def generate_report(self, days: int = 30, output_format: str = 'pdf'):
        """
        Generate safety report
        
        Args:
            days (int): Number of days to include in report
            output_format (str): Output format ('json', 'pdf', 'csv')
        """
        logger.info(f"Generating safety report for last {days} days...")
        
        latest = self.analytics.get_latest_history_record()
        if not latest:
            logger.warning("No historical analytics available to generate a report.")
            return None

        safety_score = float(latest.get('safety_score', 0.0))
        risk_level = latest.get('risk_level', 'N/A')
        grade = latest.get('safety_grade', 'N/A')
        recommendations = self.analytics.get_recommendations(
            int(latest.get('helmet_violations', 0)),
            int(latest.get('vest_violations', 0)),
            safety_score
        )

        summary = {
            'safety_score': safety_score,
            'safety_grade': grade,
            'risk_level': risk_level,
            'workers': int(latest.get('workers', 0)),
            'total_violations': int(latest.get('total_violations', 0)),
            'helmet_violations': int(latest.get('helmet_violations', 0)),
            'vest_violations': int(latest.get('vest_violations', 0)),
            'hazard_entries': int(latest.get('hazard_entries', 0)) if latest.get('hazard_entries') is not None else 0,
            'compliance_percentage': float(latest.get('compliance_percentage', 0.0)),
            'accident_probability': latest.get('accident_probability', 0.0)
        }

        output_path = Path(__file__).resolve().parent / 'reports' / f'safety_report_{days}days.{output_format}'
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if output_format == 'pdf':
            self.report_generator.generate_pdf(summary, recommendations, str(output_path))
        else:
            self.analytics.export_analytics_report(str(output_path), days=days)

        logger.info(f"Report generated at: {output_path}")
        return output_path


def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='AI Construction Site Safety Platform')
    
    parser.add_argument(
        '--mode',
        type=str,
        choices=['detection', 'dashboard', 'report'],
        default='dashboard',
        help='Mode to run the application'
    )
    
    parser.add_argument(
        '--video-source',
        type=str,
        default='0',
        help='Video source (webcam index, video file path, or RTSP stream)'
    )
    
    parser.add_argument(
        '--output-path',
        type=str,
        default=None,
        help='Output path for video or report'
    )
    
    parser.add_argument(
        '--model-path',
        type=str,
        default=str(Path(__file__).resolve().parent / 'models' / 'safety_detection' / 'weights' / 'best.pt'),
        help='Path to trained model'
    )
    
    parser.add_argument(
        '--device',
        type=str,
        default='cuda:0',
        help='Device to use (cuda:0, cuda:1, cpu)'
    )
    
    parser.add_argument(
        '--report-days',
        type=int,
        default=30,
        help='Number of days for report generation'
    )
    
    args = parser.parse_args()
    
    # Initialize platform
    platform = SafetyPlatform(model_path=args.model_path, device=args.device)
    
    # Run based on mode
    if args.mode == 'detection':
        video_source = int(args.video_source) if args.video_source.isdigit() else args.video_source
        platform.run_detection(video_source=video_source, output_path=args.output_path)
        
    elif args.mode == 'dashboard':
        platform.run_dashboard()
        
    elif args.mode == 'report':
        platform.generate_report(days=args.report_days)
        
    else:
        logger.error(f"Unknown mode: {args.mode}")
        sys.exit(1)


if __name__ == "__main__":
    main()
